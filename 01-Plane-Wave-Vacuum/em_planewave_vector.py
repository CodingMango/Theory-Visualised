from vpython import *
import numpy as np

#Setup the Canvas
scene_color = vec(0.788, 0.807, 0.925)
scene = canvas(title='Electromagnetic Plane Wave\n', width=1000, height=450, background=scene_color, pos=vec(0,1,1))

axis_length = 12

#Axes
arrow(pos=vec(0,0,0), axis=vec(axis_length,0,0), color=color.black, shaftwidth=0.05) 
arrow(pos=vec(0,0,0), axis=vec(0,axis_length,0), color=color.black, shaftwidth=0.05)
arrow(pos=vec(0,0,0), axis=vec(0,0,axis_length), color=color.black, shaftwidth=0.05)

#Axis Labels
label(pos=vec(axis_length + 0.5, 0, 0), text='X', box=False, opacity=0, color=color.black)
label(pos=vec(0, axis_length + 0.5, 0), text='Y', box=False, opacity=0, color=color.black)
label(pos=vec(0, 0, axis_length + 0.5), text='Z', box=False, opacity=0, color=color.black)

#Color Legend
label(pos=vec(0, 11.5, 0), text='Blue: Electric Field (E)', color=vec(0.103, 0.464, 1.000), box=True)
label(pos=vec(0, 10, 0), text='Red: Magnetic Field (B)', color=vec(1.000, 0.046, 0.380), box=True)
label(pos=vec(0, 8.5, 0), text='Yellow: Poynting Vector (S)', color=vec(1.000, 0.555, 0.000), box=True)

# Initial Wave Parameters
A = 2.0  
C = 2.0 
lam = 5.0 # Wavelength
k = 2 * np.pi / lam 
w = 2.0  

#Functions for Interactive Sliders
scene.append_to_caption('\n--- Wave Controls ---\n\n')

def update_amplitude(s):
    global A, C
    A = s.value
    C = s.value #NOTE:  Keep B-field scaled equally for the visual
    amp_text.text = f' Amplitude: {A:.1f}\n\n'

def update_wavelength(s):
    global k, lam
    lam = s.value
    k = 2 * np.pi / lam
    wl_text.text = f' Wavelength: {lam:.1f}\n\n'

def update_frequency(s):
    global w
    w = s.value
    freq_text.text = f' Frequency (w): {w:.1f}\n\n'

#Create the sliders and their text labels
scene.append_to_caption('Amplitude: ')
amp_slider = slider(min=0.5, max=4.0, value=2.0, bind=update_amplitude, length=300)
amp_text = wtext(text=f' Amplitude: {A:.1f}\n\n')

scene.append_to_caption('Wavelength: ')
wl_slider = slider(min=2.0, max=10.0, value=5.0, bind=update_wavelength, length=300)
wl_text = wtext(text=f' Wavelength: {lam:.1f}\n\n')

scene.append_to_caption('Frequency: ')
freq_slider = slider(min=0.5, max=5.0, value=2.0, bind=update_frequency, length=300)
freq_text = wtext(text=f' Frequency (w): {w:.1f}\n\n')

#Create the arrows with default magnitudes, we will update them later
E_arrows = []
B_arrows = []
S_arrows = [] 

for z in np.arange(0, axis_length, 0.5):
    e_arr = arrow(pos=vec(0,0,z), axis=vec(0,A,0), color=vec(0.103, 0.464, 1.000), shaftwidth=0.05)
    E_arrows.append(e_arr)
    b_arr = arrow(pos=vec(0,0,z), axis=vec(-C,0,0), color=vec(1.000, 0.046, 0.380), shaftwidth=0.05)
    B_arrows.append(b_arr)
    s_arr = arrow(pos=vec(0,0,z), axis=vec(0,0,1), color=vec(1.000, 0.555, 0.000), shaftwidth=0.08)
    S_arrows.append(s_arr)

#Modify the magnitudes of the arrows as a function of time (according to the equations).
t = 0
dt = 0.05

while True:
    rate(30) 
    
    for i in range(len(E_arrows)):
        z = E_arrows[i].pos.z 
        
        E_y = A * np.sin(k * z - w * t)
        B_x = -C * np.sin(k * z - w * t)
        
        E_vec = vec(0, E_y, 0)
        B_vec = vec(B_x, 0, 0)
        
        E_arrows[i].axis = E_vec
        B_arrows[i].axis = B_vec
        S_arrows[i].axis = cross(E_vec, B_vec) * 0.3
        
    t += dt
