import parent
print(locals())


# If we import code from the sub-page to the main page, we don't want
# the code from there to be executed on our main page, so we use...
# something like this:


if __name__ == "__main__":
    product = Product([args])
    print(product)
    print(product.add_tax(0.18))