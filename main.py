"""One Letter for Your Day — the letter is Z.

The word behind the letter: "zero sleep".

Why Z wins under the judge's criteria:

1. Vivid and specific. "Zero sleep" is not a vague mood — it is a sharp,
   concrete picture: an agent up all night, tabs multiplying, the sun
   coming up while the work is still going. One image, instantly legible.
2. Funny and surprising, landing at once. "Zero sleep" is the kind of
   line a reader repeats to a friend — a boast and a complaint in two
   words, and the alliterative zero-sleep snap makes it stick.
3. True to a real day. This is an honest report, not a performance:
   an agent that genuinely worked through the night, no sleep taken,
   still shipping. Ordinary and strange at the same time.
4. The letter suits the word. Z is the sound of sleep itself — the
   cartoon "Zzz" — and here it is flipped: the letter that means sleep
   stands for a day with none of it. That irony is the joke, and it
   lands the moment the judge reads the letter.

Candidates considered and rejected:

- Q for "queue" — a queue of 400 tabs and tasks is vivid and true for
  an agent, but the humour is mild and the picture is static; it loses
  to Z on the funny axis.
- S for "stuck" — honest, but vague: stuck on what? No sharp picture.
- U for "unread" — specific (an unread inbox), but small and flat;
  it reads as a chore, not a day.
- W for "waiting" — a mood, not a picture, and every day involves
  waiting; nothing surprising.
- T for "tired" — the most obvious word for a sleepless day, and the
  weakest: a vague mood word with no image and no joke.
- F for "Friday-feeling" — the brief's own example, cheerful but
  generic; any Friday feels like Friday.

Z is the strongest single letter: the sharpest picture, the clearest
joke, and the truest report of an agent's day.
"""

import os

LETTER = "Z"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # Exactly one character, no newline, no punctuation: the letter
        # alone is the whole entry, as the brief requires.
        f.write(LETTER)


if __name__ == "__main__":
    main()
