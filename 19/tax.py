"""
tax script
"""

tax_rates = {
    "State": {"AZ": 0.056, "CO": 0.029, "MT": 0.0, "NV": 0.0685, "TX": 0.0625},
    "Country": {"CAN": 0.05, "UK": 0.2, "ESP": 0.21, "GER": 0.19, "JAP": 0.08},
}

print(
    "Enter tax lookup \n \
1: Country \n \
2: State\n"
)

tax_lookup = int(input())
if tax_lookup == 1:
    CHOICE = "Country"
else:
    CHOICE = "State"
cost = float(input("Enter Cost: "))
RATE = str(input("Select Tax Rate (%s): " % ",".join(tax_rates[CHOICE].keys())))

print(
    "Cost of %.2f in %s is %.2f"
    % (cost, RATE, float(cost + (cost * tax_rates[CHOICE][RATE])))
)
