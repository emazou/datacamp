from sqlalchemy import create_engine, MetaData, Table, select, and_
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

engine = create_engine("sqlite:///european_database.sqlite")
conn = engine.connect()
metadata = MetaData()
division = Table('divisions', metadata, autoload=True, autoload_with=engine)
match = Table('matchs', metadata, autoload=True, autoload_with=engine)

query = select([division, match]).\
    select_from(division.join(match, division.columns.division == match.columns.Div)).\
        where(and_(division.columns.division == "E1", match.columns.season == 2009)).\
        order_by(match.columns.HomeTeam)

output = conn.execute(query)
results = output.fetchall()
data = DataFrame(results)
data.columns = results[0].keys()
data.to_csv("SQL_result.csv",index=False)

f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation=90)
sns.set_color_codes("pastel")
sns.barplot(x="HomeTeam", y="FTHG", data=data,
            label="Home Team Goals", color="#52B8B6")

sns.barplot(x="HomeTeam", y="FTAG", data=data,
            label="Away Team Goals", color="#B852A8")
ax.legend(ncol=2, loc="upper left", frameon=True)
ax.set(ylabel="FTHG", xlabel="HomeTeam")
ax.set_title("Data Visualization")
sns.despine(left=True, bottom=True)
plt.show()

