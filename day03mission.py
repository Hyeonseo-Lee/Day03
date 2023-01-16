#5.5

letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.'''.format(salutation='lovely', name='Lee HanSeo', product='fan', verbed='messed', room='living room', animals='dog', amount=2, percent=70)

print(letter)



