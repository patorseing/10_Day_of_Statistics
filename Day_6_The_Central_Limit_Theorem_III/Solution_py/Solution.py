samples = 100
mean = 500
sd = 80
interval = 0.95
z = 1.96

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))
