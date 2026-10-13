"""File-buffer Go-Back-N style sliding-window demonstration."""
import argparse
import json
import time
from pathlib import Path


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")


def receiver(frames, expected, output):
    for frame in frames:
        number = frame["number"]
        if number < expected:
            continue  # An accepted retransmission must not duplicate the text.
        if number != expected:
            return {"kind": "NACK", "next": expected}, expected, output
        output += frame["data"]
        expected += 1
    return {"kind": "ACK", "next": expected}, expected, output


def simulate(message, window=3, directory=".", error_at=None,
             bad_ack_once=False, timeout_once=False, delay=0, manual=False):
    if window <= 0:
        raise ValueError("Window size must be positive")
    if error_at is not None and not 0 <= error_at < len(message):
        raise ValueError("Error frame must exist")
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    sender_file = directory / "Sender_Buffer"
    receiver_file = directory / "Receiver_Buffer"
    base = expected = attempts = 0
    output = ""
    injected = ack_injected = timed_out = False
    events = []
    while base < len(message):
        attempts += 1
        if attempts > max(20, len(message) * 5):
            raise RuntimeError("No progress: check manually edited buffer files")
        end = min(base + window, len(message))
        frames = [{"number": i, "data": message[i]} for i in range(base, end)]
        write_json(sender_file, frames)
        events.append("SEND " + json.dumps(frames))
        if error_at is not None and not injected and base <= error_at < end:
            frames[error_at - base]["number"] += 100
            write_json(sender_file, frames)
            events.append(f"INJECT incorrect number at frame {error_at}")
            injected = True
        if manual:
            input("Edit Sender_Buffer now, then press Enter: ")
        time.sleep(delay)
        frames = json.loads(sender_file.read_text())
        ack, expected, output = receiver(frames, expected, output)
        write_json(receiver_file, ack)
        events.append(f"RECEIVER {ack['kind']} {ack['next']}")
        if timeout_once and not timed_out:
            events.append("TIMEOUT: feedback discarded; resend current window")
            timed_out = True
            continue
        if bad_ack_once and not ack_injected:
            write_json(receiver_file, {"kind": "ACK", "next": end + 100})
            ack_injected = True
        if manual:
            input("Edit Receiver_Buffer now, then press Enter: ")
        ack = json.loads(receiver_file.read_text())
        k = ack.get("next")
        valid = isinstance(k, int) and (
            ack.get("kind") == "ACK" and base < k <= end or
            ack.get("kind") == "NACK" and base <= k < end)
        if not valid:
            events.append("INVALID feedback: resend current window")
            continue
        events.append(f"{ack['kind']} {k}")
        base = k
    return output, events


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--text", default="NETWORK")
    p.add_argument("--window", type=int, default=3)
    p.add_argument("--directory", default=".")
    p.add_argument("--error-at", type=int)
    p.add_argument("--bad-ack-once", action="store_true")
    p.add_argument("--timeout-once", action="store_true")
    p.add_argument("--delay", type=float, default=0)
    p.add_argument("--manual", action="store_true")
    a = p.parse_args()
    output, events = simulate(a.text, a.window, a.directory, a.error_at,
                             a.bad_ack_once, a.timeout_once, a.delay, a.manual)
    print("\n".join(events))
    print("Recovered:", output)


if __name__ == "__main__":
    main()
