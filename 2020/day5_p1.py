data_file = 'day5/input'

max_seat_id = 0
boarding_pass_ids = []

with open(data_file, 'r') as input:
    for line in input:
        num_rows = 128

        rows = list(range(num_rows))
        lower = rows[0]
        upper = rows[-1]

        for i in range(7):
            num_rows = int(num_rows / 2)
            if line[i] == 'F':
                rows = rows[0:num_rows]
            else:
                rows = rows[num_rows:]

            lower = rows[0]
            upper = rows[-1]

        row = lower

        num_seats = 8
        seats = list(range(num_seats))
        for i in range(7, 10):
            num_seats = int(num_seats / 2)
            if line[i] == 'L':
                seats = seats[0:num_seats]
            else:
                seats = seats[num_seats:]

            lower = seats[0]
            upper = seats[-1]

        seat = lower

        seat_id = row * 8 + seat
        boarding_pass_ids.append(seat_id)

        if seat_id > max_seat_id:
            max_seat_id = seat_id

print(f"Part 1: {max_seat_id}")

boarding_pass_ids.sort()
#print(boarding_pass_ids)

your_seat = [i for i in range(max_seat_id) if i not in boarding_pass_ids if i + 1 in boarding_pass_ids if i - 1 in boarding_pass_ids]
print(f"Part 2: {your_seat}")