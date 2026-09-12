# Clockodo Autofiller

A small Python/Selenium script that logs into [Clockodo](https://www.clockodo.com/)
and automatically fills in a standard working-day time entry (start, end, break start
and break duration), so you don't have to type the same times by hand every day.

## What it does

- Opens Clockodo in a Selenium-controlled Brave/Chrome browser.
- Logs in with your credentials.
- Opens the "add time entry" form and fills in a fixed shift: 07:30–17:00 with a
  60-minute break starting at 12:00.
- Clicks **Speichern** to save the entry.

The times and login details are hard-coded near the top of `main.py` — edit them to
match your own schedule before running.

## Tech

- Python 3
- [Selenium](https://pypi.org/project/selenium/) WebDriver
- A Chromium-based browser (configured for Brave) plus a matching ChromeDriver

## Run

```bash
pip install selenium
python main.py
```

Update these in `main.py` first:

- `driver_path` — path to your ChromeDriver executable.
- `options.binary_location` — path to your browser binary.
- The email and password used to log in.

> Note: credentials are entered in plain text in the script. Keep the file private and
> do not commit real passwords.
