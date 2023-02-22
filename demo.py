"""
demo.py
Spring 2023

Demonstrate some features of REs and Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

#%%

#
#  A few RE examples using the demo.csv file
#

demo = pd.read_csv('demo.csv',dtype=str)

#
#  Drop records with missing data for Meeting Days. Make a copy of the new
#  dataframe so we can add columns later.
#

trim = demo.dropna(subset="Days")
trim = trim.copy()

#
#  Look for specific contents in a string
#

has_AM = trim['Time'].str.contains("AM")
print( trim[ has_AM ] )

has_AMPM = trim['Time'].str.contains("AM.*PM")
print( trim[ has_AMPM ] )

is_TT = trim['Days'].str.contains(r"Tu|Th")
print( trim[ is_TT ] )

is_LD = trim['Number'].str.contains(r"^1|^2")
print( trim[ is_LD ] )

ends_0or5 = trim['Number'].str.contains(r"0$|5$")
print( trim[ is_LD & ends_0or5 ] )

#
#  Split a string into a list using an RE and store the list in a
#  column of a dataframe
#

trim['Split'] = trim["Time"].str.split(r":| - | ")

#
#  Split a string into a list using an RE and create a new dataframe
#  from the pieces
#

exp = trim["Time"].str.split(r":| - | ", expand=True)


#%%

#%%

#  Set the default figure resolution

plt.rcParams['figure.dpi'] = 300

#  Read in ETR data from the earlier assignment

hh_data = pd.read_csv('etrs.csv')

#%%

#
#  Draw a basic histogram
#

fig0,ax0 = plt.subplots()

hh_data['etr'].plot.hist(ax=ax0,bins=20,title='Distribution of ETRs')

ax0.set_xlabel('ETR')

fig0.tight_layout()

#%%

#
#  Draw a two-panel plot
#

fig2, (ax21,ax22) = plt.subplots(1,2)

medians = hh_data.median()

hh_data.plot.scatter(ax=ax21,x='inc',y='etr',title='ETR vs Income')

ax21.set_xlabel('Income')
ax21.set_ylabel('ETR')

ax21.axhline(medians['etr'], c='r', ls='--', lw=1)
ax21.axvline(medians['inc'], c='r', ls='--', lw=1)

hh_data['etr'].plot.hist(ax=ax22,bins=20,title='Distribution of ETRs')

ax22.set_xlabel('ETR')

fig2.suptitle('Pooled Data')
fig2.tight_layout()

#%%

#
#  Draw a four panel plot with two rows and two columns. In this
#  form, the Axes objects will be stored in array axs, which will
#  have 2 rows and 2 columns.
#

tidy_data = hh_data.rename(columns={'inc':'Income','etr':'ETR'})

fig3, axs = plt.subplots(2,2,sharex=True,sharey=True)

tidy_data.query('type==1').plot.scatter(ax=axs[0,0],x='Income',y='ETR',title='Type 1')
tidy_data.query('type==2').plot.scatter(ax=axs[0,1],x='Income',y='ETR',title='Type 2')
tidy_data.query('type==3').plot.scatter(ax=axs[1,0],x='Income',y='ETR',title='Type 3')
tidy_data.query('type==4').plot.scatter(ax=axs[1,1],x='Income',y='ETR',title='Type 4')

fig3.suptitle('Income and ETR Data by Type')
fig3.tight_layout()

#%%

#
#  Draw a scatterplot that uses a third variable for color coding
#  the points
#

fig4,ax4 = plt.subplots()
tidy_data.plot.scatter(ax=ax4,x='Income',y='ETR',c='type',cmap='viridis')
fig4.tight_layout()
