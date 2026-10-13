import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pixel_cafe_sales.csv')
# print(df)

 # print(df.shape) # (number of rows, numbers of columns)
# print(df.columns) # (prints names of the columns)

# print(df[["Product", "Quantity"]]) # prints certain columns

# 3.filter: display food rows
# food = df[df["Category"] == "Food"]
# print(food)

# then display al rows with quantities greater than 30
# busy = df[df["Quantity"] > 30] 
# print(busy)

# only food items over 30
# both = df[(df["Quantity"] > 30) & (df["Category"] == "Food")]
# print(both)

# 4. sort: display the the rows with the largest quantities
# ranked = df.sort_values("Quantity", ascending=False)
# print(ranked.head(3))

# 4. sort: display the the rows with the smallest quantities
# ranked = df.sort_values("Quantity", ascending=True)
# print(ranked.head(3))

# 5. calculate: add revenue = price * quantity
# df["Revenue"] = df["Price"] * df["Quantity"]
# print(df[["Product", "Price", "Quantity", "Revenue"]])

# 6. summarise: display the total revenue in pounds
# df["Revenue"] = df["Price"] * df["Quantity"]
# total_revenue = df["Revenue"].sum()
# print(f"Total revenue: £{total_revenue:.2f}")  

# A. Display all Friday rows.
# friday = df[df["Day"] == "Friday"]
# print(friday)

# B. Find friday's total revenue.
# df["Revenue"] = df["Price"] * df["Quantity"] # calculated above
# friday = df[df["Day"] == "Friday"]
# friday_revenue = friday["Revenue"].sum()
# print(f"Friday's total revenue: £{friday_revenue:.2f}")

# C. Display the five rows with the highest revenue.
# highest_revenue = df.sort_values("Revenue", ascending=False)
# print(highest_revenue.head(5))

# D. find total food revenue for the week
# df["Revenue"] = df["Price"] * df["Quantity"] # calculated above
# food = df[df["Category"] == "Food"]
# food_revenue = food["Revenue"].sum()
# print(f"weekly food revenue: £{food_revenue:.2f}")

# E. Write a recommendation using two figures.
# Students should write their own recommendation.

df["Revenue"] = df["Price"] * df["Quantity"]
friday = df[df["Day"] == "Friday"]
food = df[df["Category"] == "Food"]
food_revenue = food["Revenue"].sum()
friday_revenue = friday["Revenue"].sum()
print(f"I recommend checking food stock before Friday. "
f"Friday generated £{friday_revenue:.2f} across all categories, "
f"and Food generated £{food_revenue:.2f} over the week. "
f"We should check Friday's food sales before deciding "
f"how much extra stock to order." )

# Optional: group by Product to compare weekly revenue totals.
weekly_revenue = df.groupby("Product")["Revenue"].sum()
print(weekly_revenue.sort_values(ascending=False).round(2))

# sets the size of your chart in Matplotlib to 6 inches wide and 4 inches tall
# plt.figure(figsize=(6,4))

# groups values into 10 bins
# plt.hist(df["Day"], bins=10)

# sets line colour and legend label
# plt.plot(x, y, color="red", label="Day")

#labels the x axis and the y axis
plt.xlabel("product")
plt.ylabel("quantity")

# rotates x-axis labels
# plt.xticks(rotation=45)

#rotates y-axis labels
# plt.yticks(rotation=45)

# gives the chart a title
plt.title("cafe sales")


# displays labels set when plotting
plt.legend(["quantity sold"])

#adjusts spacing to fit labels
# plt.tight_layout()

# displays grid line
# plt.grid(True)

# creates a chart with the data selected as a line graph
# plt.plot(df["Day"], df["Category"])

# creates a chart with the data selected as a bar graph
plt.bar(df["Product"], df["Quantity"])

# creates a chart with the data selected as a scatter graph 
# plt.scatter(df["Day"], df["Category"])

# only shows monday
# monday_data = df[df["Day"] == "Monday"]
# plt.bar(monday_data["Day"], monday_data["Category"])

# only shows monday and tuesday
# selected_days = df[df["Day"].isin(["Monday", "Tuesday"])]
# plt.bar(selected_days["Day"], selected_days["Category"])



# displays chart
plt.show()

# closes current figure
# plt.close()