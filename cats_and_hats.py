cats = {}
for cat in range(1,101):
    cats.update({cat:"hat off"})


for num in range(1,101):
    for cat in cats:
        if cat % num == 0:
            if cats[cat] == "hat off":
                cats[cat] = "hat on"
            else:
                cats[cat] = "hat off"

for cat in cats:
    if cats[cat] == "hat on":
        print(f"Cat {cat} has a {cats[cat]}.")
