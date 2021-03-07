## Team12 Project
# PaperGap_Wallet

Secure Live-Boot Environment For Bitcoin Paper Wallet Generation
This app creates a live bootable USB linux distribution. When booted shows a simplstic one-app system, completely air-gapped with no networking intefaces
and no desktop environment. A simplistic UI created using Pythons frontend framework Kivi will help the user create/restore a valid bitcoin wallet in the 
simplest and easiest way possible, while being completely secure at the same time.

### Authors
```
Ozzak Matic
Oliver Cunnington
Robert O'Brien
John Furlong
Janine Dunlea
```

### Prerequisites

* [Installing Python](https://www.python.org/downloads/) - Installing Python
* [Kivi Install Pycharm](https://www.youtube.com/watch?v=RYF73CKGV6c&list=PLhTjy8cBISEpobkPwLm71p5YNBzPH9m9V) - Installing Kivy On Pycharm
* [Kivi Install Windows](https://kivy.org/doc/stable/installation/installation-windows.html) - Installing Kivy On Windows
* [Kivi Install Other Platforms](https://kivy.org/doc/stable/gettingstarted/installation.html) - Installing Kivy on all other platforms (including linux, mac, pip, conda etc)
* [Bitcoin Library Install](https://github.com/primal100/pybitcointools) - Installing Bitcoin tools (see Readme on Linked github page)



Will be running on a USB linux distribution


### Built With

* [Kivi](https://kivy.org/#home) - The  Python Frontend framework used
* [Bitcoin Tool](https://github.com/primal100/pybitcointools) - Bitcoin wallet code
* [Linux Distro](http://linuxfromscratch.org/lfs/view/stable/index.html) - Linux Distro Information

### Progress Of Project
#### Frontend
Frontend fully integrated with bitcoin library code. Now working towards PDF generation and Unit testing.

#### Bitcoin wallet code
Wallet restoration feature implemented, focusing on adding other kinds of crypto wallets.

#### Linux Distro
A test version of distro is already up and running with all network interfaces disabled. Will be working towards integrating the dependency sizes into the distro.





# User Guide

## Installation
-	TODO


## Application walk-through

### Step 1
Upon running the app you will land on our "wellcome page" there are only 2 options to choose from here
1. **Create a New Wallet**: choose this one if you are first time user and don't have an existing wallet seed. If you choose this option go to Step 2
2. **Restore Previous Wallet**: choose this one if you already have a seed and wish to generate more addresses from the same seed. If you choose this option go to Step 4

<a href="https://ibb.co/XbZ2HLS"><img src="https://i.ibb.co/6mRnQwg/1.png" alt="1" border="0"></a>

### Step 2
Now you need to specify what type of wallet/seed you wish to generate.
There are three dropdown menus: 
1. **Coin Type**: only Bitcoin works at the moment
2. **Word Number**: there are 4 options: 12, 16, 20 and 24. We recommend using **24 words** as the safest option. Alternatively if you are using some of the older wallets as your hot wallet choose 12 words. (like Electrum for example).
3. **Mnemonic Language**: there are 3 options: English, Spanish and French. Pick one you are most comfortable with.

After choosing the options click **Generate Wallet** and go to Step 3

<a href="https://ibb.co/r3Rtwgq"><img src="https://i.ibb.co/gdL7RGQ/4.png" alt="4" border="0"></a>


### Step 3

This step is **VERY important.** Your "recovery phrase" represents your seed which is used to generate your PRIVATE keys.

Your PRIVATE keys need to be PRIVATE and kept a secret!

**Do not** enter them on any machine with network access.

**Do not** lose them (you will lose your Bitcoin).

**Do not** share them with anyone.

Use **pen and paper** to write down the seed by hand. And **store the paper** in a safe and dry place.


<a href="https://ibb.co/dGHzqB0"><img src="https://i.ibb.co/BqYSxLV/6.png" alt="6" border="0"></a>

Example:

<a href="https://ibb.co/Hqrkdw8"><img src="https://i.ibb.co/yq8bSvj/seed.jpg" alt="seed" border="0"></a>

After writing down the seed tick the box *"I have safely stored my recovery phrase offline"* and click **Continue to Wallet** and go to Step 4

### Step 4

Here you will need to enter the seed you just wrote down back to the application to confirm that you stored it correctly.
After clicking **Submit Phrase** if you entered the seed correctly the application will forward you to the next screen, and go to Step 5

- If you didn't generate the seed now (steps 2 and 3) but are using previously generated seed (came here from step 1) enter that previously generated seed now.


<a href="https://ibb.co/mtGzymZ"><img src="https://i.ibb.co/XpbJ590/20.png" alt="20" border="0"></a>


### Step 5

At this stage we are almost there. The applicaton will offer you to choose the number of PUBLIC addresses asociated with the PRIVATE seed/key you provided.

Public addresses will be stored in a .pdf file and are safe to share.

You will use them to send Bitcoin to your wallet.

We recommend choosing 50 or 100 to increase privacy (use different one every time you send yourself Bitcoin)

<a href="https://ibb.co/nkn56Pc"><img src="https://i.ibb.co/RHBVYj0/10.png" alt="10" border="0"></a>

After choosing a number of addresses tick *"Add QR code"* box to the wallet easier to use. And enter a name/label for your waller (example "MyPaperWallet_01")


<a href="https://ibb.co/QXK5x9c"><img src="https://i.ibb.co/0QGwzqX/11.png" alt="11" border="0"></a>

### Step 6

.pdf file will be ??
- TODO




