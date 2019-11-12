# Work
Most of the work was done in a Jupyter Notebook because I would normally be running this in Airflow.  I took my standard coding practices and used them, but as of 11 November 2019, 10:56 PM PST, I have done this in Python.  The code is of high-quality, and I will be switching over to Postgres as the main tool, but this was simply done to get the answer out quick, while having strong quality around the ingestion.

# Answers
1.  Unique users:  2904
2.  Marketing providers:  Facebook, Instagram, Spotify, Snapchat, Inst
3.  Most-changed Attribute - Name:  {most_changed_attribute_name}, Count:  {most_changed_attribute_count}
4.  Users shown an ad on Snapchat on 2019-07-03:  261
5.  Ad shown most to moderates:  4
5.  Ad shown most to moderates:  4
6.  See below:
```
marketing_df.groupby(by=["ad_id"])\
    .agg({"length": ["mean", "std"], "phone_id": "nunique"})\
    .sort_values([
        ('phone_id', "nunique"),
        ("length", "mean")],
    ascending=False)
```

# Examining the data output from the above Python code, it appears clear that there are 4 ad groups based upon the number of users an ad was shown to
## Because of this, there appears to be a winner for each group, and then we will select another
### Group 1:  >500 users shown
Winner:  ad_id = 0
Reason:  mean - 2 std. dev > every other in the group
### Group 2:  300-499 users shown
Winner:  ad_id = 5
Reason:  mean - 2 std. dev > every other in the group
### Group 4:  160-299 users shown
Winner:  ad_id = 12
Reason:  mean - 2 std. dev > every other in the group
### Group 3:  100-159 users shown
Winner:  ad_id = 14
Reason:  mean - 2 std. dev > every other in the group
### Group 4:  <100 users shown
Winner:  ad_id = 20
Reason:  mean - 2 std. dev > every other in the group
