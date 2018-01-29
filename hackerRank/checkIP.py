# << Swami Shreeji >>
# @nishantpatel
# Complete the function below. Check if IPv4 or IPv6 - HackerRank challenge

import sys
import os
import string

def checkIP(ip):
    ans = []
    countDot = 0
    countCol = 0
    for ele in ip:
        countDot = ele.count(".") 
        countCol = ele.count(":")
            
        if countDot < 3 and countCol < 7:
            ans.append("Neither")
            
        elif countDot == 3: 
            testIpv4 = ele.split(".")
            
            for char in testIpv4:
                if char.isalpha():
                    ans.append("Neither")
                else:
                    testIpv4 = map(int, testIpv4)
                    for ele in testIpv4:
                        if ele < 0 or ele > 255:
                            ans.append("Neither")
                        else:
                            ans.append("IPv4")
                            break
                    break
                    
        elif countCol == 7:
            testIpv6 = ele.split(":")
            for ele in testIpv6:
                if all(char in string.hexdigits for char in ele):
                    ans.append("IPv6")
                else:
                    ans.append("Neither")
                break
           
    return ans