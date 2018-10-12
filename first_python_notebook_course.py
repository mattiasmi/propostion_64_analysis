import pandas as pd

props = pd.read_csv("committees.csv")
contribs = pd.read_csv("contributions.csv")

# This finds a count of the props_name and .rest_index() makes it a clean table
#print(props.prop_name.value_counts().reset_index())

# Filtering a Data Frame
# Isolating Proposition 64 to find propositions related to biggest donors for and against drug legalization

prop = props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

merged = pd.merge(prop, contribs, on="calaccess_committee_id")


#This will show all of the headers of the table in a series
##print(merged.head(0))

# print all of the values in a column
##print(merged.amount)
print("total amount:",merged.amount.sum())
# Recognize the limits of the data set itself; for example, this is a lower number because in California you only have to disclouse for 100 or more
#--refer to this data as only including large donors
support = merged[merged.committee_position == 'SUPPORT']
oppose = merged[merged.committee_position == 'OPPOSE']

print("oppose amount:",oppose.amount.sum())
print("support amount:",support.amount.sum())

print("Percentage of support",(support.amount.sum() / merged.amount.sum())*100)
print("Percentage of oppose",(oppose.amount.sum() / merged.amount.sum())*100)

# Note that returns the DataFrame resorted in ascending order from lowest to highest. That is pandas default way of sorting.
merged.sort_values("amount")
# Make it largest to smallest and add .head() to only show top 5
'''
top5_amount = merged.sort_values("amount", ascending=False).head()
print(top5_amount)

print(support.sort_values("amount", ascending=False).head())
print(oppose.sort_values("amount", ascending=False).head())
print(merged.info())
print(merged.groupby("committee_name_x").amount.sum().reset_index().sort_values("amount", ascending=False))
print(merged.groupby("committee_name_x").amount.sum().reset_index())

print(merged.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False))
'''
# What percentage of donations came from people who live outside of California?

not_ca = merged[merged.contributor_state != 'CA']
print("Percentage of funding outside of CA", (not_ca.amount.sum() / merged.amount.sum())*100)

#This is a list of the top contributors from outside the state and their position
print(not_ca.groupby([ "contributor_state", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False))

#print(not_ca.groupby(["contributor_firstname", "contributor_lastname", "committee_position"].amount.sum().reset_index().sort_values("amount", ascending=False))
top_supporters = support.groupby(
    ["contributor_firstname", "contributor_lastname"]
).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)

top_supporters['contributor_fullname'] = top_supporters.contributor_firstname + " " + top_supporters.contributor_lastname
