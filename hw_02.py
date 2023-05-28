def game(lists, power):
    total_energy = 0

    for sublist in lists:
        sublist_energy = 0

        for energy in sublist:
            if energy <= power:
                sublist_energy += energy
                power -= energy
            else:
                break

        total_energy += sublist_energy

        if sublist_energy > power:
            break

    return total_energy
