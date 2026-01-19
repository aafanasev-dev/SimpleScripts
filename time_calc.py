times = [
    "0:03",
    "0:04",
    "0:05",
    "0:05",
    "0:05",
    "0:05",
    "0:04",
    "0:05",
    "0:05",
    "0:05",
    "0:06",
    "0:06",
    "0:01",
    "0:05",
    "0:03",
    "0:04",
    "0:04",
    "0:05",
    "0:05",
]

def calculate_total_time(times):

    total_minutes = 0

    for t in times:
        hours, minutes = map(int, t.split(":"))
        total_minutes += hours * 60 + minutes

    total_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    print(f"Total time: {total_hours}:{remaining_minutes:02d}")


if __name__ == "__main__":
    calculate_total_time(times)
