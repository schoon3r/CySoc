#!/usr/bin/env python3

# Author: Jim Labilles
# Date: 29 Dec 2022

#########################################################
##                    CTF Challenge                    ##
#########################################################

# Reverse Engineering Challenge
# Option 01: reverse the code
# Option 02: run the code in your terminal and programatically get the answer
#            $ python3 bee_kwik.py

import hashlib
import random
import time
import datetime

raw = 'dontbesoquicktodrawyourgunofjudgementoryouwillmissyourtarget'
raw_bytes = bytes(raw, 'utf-8')
h = hashlib.sha512(raw_bytes)
digest = h.hexdigest()
s = 'ww_yu_r_qukr_hn_bb'
flag_format = 'CySOC_FLAG{'


def get_flag():
    flag = flag_format + raw[0] + digest[4] + raw[1:4] + digest[27] + \
        raw[4:10] + digest[23] + digest[12] + digest[14] + \
        raw[10] + digest[14] + s[11:13] + digest[3] + \
        raw[13] + digest[5] + raw[14:16] + raw[17] + digest[4] + raw[17]
    return flag


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    return True


def rand_gen():
    character = random.choice(raw)
    freq = random.randint(1, 5)
    timer = random.randint(20, 30)
    return character, freq, timer


def init_fin():
    c = s[0] + digest[4] + s[1:4] + digest[27] + \
        s[4:10] + digest[23] + digest[12] + digest[14] + \
        s[10] + digest[14] + s[11:13] + digest[3] + \
        s[13] + digest[5] + s[14:16] + s[17] + digest[4] + s[17]
    return flag_format + c + '}'


if __name__ == "__main__":
    dub = rand_gen()
    now = datetime.datetime.now()
    cysoc = get_flag()
    print('\n[+] CySOC Challenge 02')
    print('[+] Be quick, quicker than the quick draw Bad Bob Munden')
    print(
        f'   [!] Enter the character "{dub[0]}", {dub[1]} times to get the flag.\n')
    key = input('[-] Enter key: ')
    after = datetime.datetime.now()
    lapsed = after - now
    if len(key) == dub[1] and key[0] == dub[0] and lapsed.seconds <= dub[2]:
        print(f'\n   [+] {init_fin()}\n')
    else:
        print('\n   Hahaha! try again noob...')
