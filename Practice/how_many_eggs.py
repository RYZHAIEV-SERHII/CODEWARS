def calculate_eggs(year: int, span: int) -> [int | str]:
    """Ronald's uncle left him 3 fertile chickens in his will. When life gives you chickens,
    you start a business selling chicken eggs which is exactly what Ronald decided to do.

    A chicken lays 300 eggs in its first year. However, each chicken's egg production
    decreases by 20% every following year (rounded down) until when it dies (after laying its quota of eggs).

    After his first successful year of business, Ronald decides to buy 3 more chickens at the start of each year.


    Your Task:

    For a given year, and life span of chicken span, calculate how many eggs Ronald's chickens will lay him that year,
    whereby year=1 is when Ronald first got his inheritance and span>0.

    If year=0, make sure to return "No chickens yet!".


    Note:

    1. All chickens have the same life span regardless of when they are bought.
    2. Let's assume all calculations are made at the end of the year so don't bother taking eggs laid per month
    into consideration.
    3. Each chicken's egg production goes down by 20% each year, NOT the total number of eggs
    produced by each 'batch' of chickens. While this might appear to be the same thing, it doesn't
    once non-integers come into play so take care that this is reflected in your kata!
    """

    # Initial Check: If year is 0, returning “No chickens yet!”.
    if year == 0:
        return "No chickens yet!"

    # Initialize Chickens: Starting with a list of three chickens, each laying 300 eggs.
    chickens = [300, 300, 300]
    total_eggs = 0

    # Looping Through Years: For each year, iterating through the chickens and calculate the total eggs.
    for y in range(1, year + 1):
        for i in range(len(chickens)):
            total_eggs += chickens[i]

            # Decreasing Production: Each chicken’s egg production decreases by 20% each year.
            chickens[i] = int(chickens[i] * 0.8)

        # Removing Old Chickens: If the current year is a multiple of span, we're removing the first three chickens.
        if y % span == 0:
            chickens = chickens[3:]

    # Returning Total: Returning the total number of eggs produced.
    return total_eggs
