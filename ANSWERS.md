# Work
Status Updates:
* 11 November 2019, 10:56 PM PST
    - Work completed in Python
* 12 November 2019, 11:56 PM PST
    - Work completed in SQL
* Open Items:
    - Documentation around functions
    - Ensure `typing` is enforced on entire repo
    - Have Dockerfile that is mainly for Python, not Jupyter
    - Have main Python file to run at boot which loads and does analysis

# Notes
Most of the work was done in a Jupyter Notebook because I would normally be running this in Airflow.  I took my standard coding practices and used them, and code is of high-quality.  The SQL may take some work, and I personally have made a heavy migration from SQL over to Scala over the past few years, so it could be improved.

# Answers
## SQL Answers (see `./docker/jupyter/notebooks/TakeHomeAssignment - Eric Meadows.ipynb`)
1.  Unique users:  2904
2.  Marketing providers:  Facebook, Inst, Instagram, Snapchat, Spotify
3.  Most-changed Attribute - Name:  drinking, Count:  1473
4.  Users shown an ad on Snapchat on 2019-07-03:  261
5.  Ad shown most to moderates:  4
6.  Data details for top-performing ads
    | user_groups | ad_id | distinct_users | view_time_mean   | view_time_percentile_1 | view_time_percentile_99 |
    |-------------|-------|----------------|------------------|------------------------|-------------------------|
    | 1           | 20    | 97             | 1237.16494845361 | -133.553648986325      | 2607.88354589354        |
    | 2           | 17    | 145            | 1162.66206896552 | -76.7608303596678      | 2402.0849682907         |
    | 3           | 12    | 173            | 1232.90173410405 | -186.057263037625      | 2651.86073124572        |
    | 4           | 5     | 379            | 1129.00527704485 | -216.018866596538      | 2474.02942068625        |
    | 5           | 0     | 673            | 1251.2823179792  | -135.78475381805       | 2638.34938977644        |
