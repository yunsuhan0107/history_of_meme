# -*- coding: utf-8 -*-
import matplotlib;
import numpy;
import matplotlib.pyplot as plt;

import csv;


# CSV file from automaton
# header =                          #need name, year
# data =                            #add meme to csv accordingly


def get_data():
    file_loc = C:\Users\ASUS\Desktop\Codeable meme\meme_data.csv
    
    with open(file_loc) as f:
    writer = csv.writer(f);
    #writer.writerow(header)         #header: name, year
    #writer.writerow(data)           #meme with name and year
    

#Visualization set up 

def visualize_scatter(filename):

  #getting information
  meme_name = x
  meme_year = y

  fig, axes = plt.subplots();
  axes.scatter(x,y);
  
  #using object API
  fig_high = plt.figure()

  #subplot with new name that declares plt.figure()
  ax_high = fig_high.add_subplot(111)

  for i in len(meme_name):
        ax_high.set_xlabel(meme_name[i], fontsize = 12)
        ax_high.set_ylabel(meme_year[i], fontsize = 12)

  #setting ticks of x
  ax_high.set_xticks(x_axis)
  ax_high.set_xticklabels(word_label, fontsize = 12, rotation = 25)

  # fig_high.bar

  ax_high.set_title('Memes and Their Corresponding Year')

  fig_high.savefig(filename)

  return meme_visual

fig_high = visualize_high(top_10, 'hightop10.png')




