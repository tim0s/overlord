Overleaf is a great tool to collaboratively write scientific articles. 
Except if your article includes plots or other generated artwork: You are in a cycle of 
* generate a new version of a plot locally
* upload it as a pdf to your overleaf project

This module aims to automate the second step. 

If you use python to generate your plot as myplot.pdf for your MyGreatResearch project on overleaf.com, where you save this plot in the folder plots you can add something like

```
# create your plot, i.e., with seaborn
plt.savefig("myplot.pdf")

# upload it
from overlord import overlord
ol = overlord()
ol.upload_file("MyGreatResearch", "plots", "myplot.pdf")
```

To login to overleaf this module needs your username/email and password. You could pass them as arguments to the upload_file() function. But that would probably lead to your password being comitted to your projects git repo by accident at some point. So overlord also checks for a YAML file in ~/.config/overlord with an email and password attribute:

```
email: 'tim0s42@inf.ethz.ch'
password: 'ThisIsMyPassword'
```
