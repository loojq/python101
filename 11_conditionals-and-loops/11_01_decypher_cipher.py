# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""
a = "abcdefghijklmnopqrstuvwxyz"
only_alphas = ""
for i in secret:
    if i in a:
        only_alphas+=i
print(str(only_alphas))