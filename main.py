import distro

print("Main Directory\n")

for k, v in distro.lsb_release_info().items():
    print(f"{k}: {v}")
