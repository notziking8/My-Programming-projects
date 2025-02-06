"""
Zion King
Comp168-004
2/15/24
In this program I will be calculating federal taxes owed or refund given wages, taxable interest,
unemployment compensation, marital status and taxes withheld and income less than 120,000 dollars.
"""
import math
wages = int(input())
taxable_interest = int(input())
unemployment_compensation = int(input())
marital_status = int(input("(1 single / 2 married) :"))
taxes_withheld = int(input())

# AGI calculation and if over 120000, print 'error'.
agi = (wages + taxable_interest + unemployment_compensation)
if agi > 120000:
    print("Error")

# Gets the deduction value.
deduction = 0
if marital_status == 1:
    deduction = 12000
elif marital_status == 2:
    deduction = 24000
else:
    marital_status = 1
    deduction = 12000
taxable_income = agi - deduction

if taxable_income < 0:
    taxable_income = 0
    print(f'Taxable Income: {taxable_income:}')

# Calculation tax amount based on marital status if single
federal_tax = 0
if marital_status == 1:
    if 0 < wages <= 10000:
        federal_tax = wages * 0.1
    elif 10000 < wages <= 40000:
        federal_tax = 1000 + (taxable_income - 10000) * 0.12
    elif 40000 < wages <= 85000:
        federal_tax = 14500 + (taxable_income - 85000) * 0.24
    elif wages > 85000:
        federal_tax = 14500 + (taxable_income - 85000) * 0.24

# Calculation tax amount based on marital status if married
elif marital_status == 2:
    if 0 < wages <= 20000:
        federal_tax = (wages * .10)
    elif 20000 < wages <= 80000:
        federal_tax = 2000 + (taxable_income - 20000) * 0.12
    elif wages > 80000:
        federal_tax = 9200 + (taxable_income - 80000) * 0.22

# Calculates the amount of taxes that are due
tax_refund = federal_tax - taxes_withheld
if tax_refund < 0:
    tax_refund = 0


print(f'AGI: ${agi:,}')
print(f'Deduction: ${deduction:,}')
print(f'Taxable income: ${taxable_income:,}')
print(f'Federal tax: ${int(round(federal_tax)):,}')
print(f'Tax due: ${int(round(tax_refund)):,}')

