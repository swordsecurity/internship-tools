import datetime as dt

# Dutch dates
import locale
locale.setlocale(locale.LC_TIME, "nl_NL") # swedish

title = "Dagenverantwoording juni 2018"
start = dt.date( 2018, 6,1  )
end = dt.date( 2018, 6, 15 )

werkzaamheden = "Orientatiefase"
skip = [
        dt.date(2018, 6, 14).strftime('%Y-%m-%d'),
]

from dateutil.rrule import DAILY, rrule, MO, TU, WE, TH, FR

def daterange(start_date, end_date):
  return rrule(DAILY, dtstart=start_date, until=end_date, byweekday=(MO,TU,WE,TH,FR))

print("# %s" % title)
print("| **Datum** | **Aard van de werkzaamheden** | **Gewerkt?** | **Aantal uur** |")
print("|--|--|--|--|")
dagen_totaal = 0
uren_totaal = 0
for item in daterange(start,end):
    if item.strftime('%Y-%m-%d') in skip: continue
    d = dt.datetime.strptime(str(item),"%Y-%m-%d %H:%M:00")
    dstr = dt.datetime.strftime(d,"%a %b %d, %Y")
    gewerkt = "Ja"
    uren = 8
    dagen_totaal += 1
    uren_totaal += uren
    print("| %s | %s | %s | %s |" % (dstr,werkzaamheden,gewerkt,str(uren)))
print("")
print("Dagen totaal: **%s**" % dagen_totaal)
print("")
print("Uren totaal: **%s**" % uren_totaal)
