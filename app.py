#!/usr/bin/env python3

from aws_cdk import core as cdk

from factorial_calculator.factorial_calculator_stack import FactorialCalculatorStack


app = cdk.App()
FactorialCalculatorStack(
    app,
    "FactorialCalculatorStack",
    env=cdk.Environment(account="251999085741", region="eu-central-1"),
)

app.synth()
