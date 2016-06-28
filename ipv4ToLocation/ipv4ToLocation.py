import os
import socket
import struct
import sys


class IPv4toLocation(object):
    def __init__(self):
        dbFile = os.path.join(os.path.dirname(__file__), 'ipv4wry.dat')
        self.ip = 0
        self.ipFile = open(dbFile, 'rb')

    def __ipToLong(self, strIP):
        return struct.unpack('!L', socket.inet_aton(strIP))[0]

    def __readIPArray(self):
        num = self.__readLongX(4)
        num3 = int((self.__readLongX(4) - num) / 7) + 1
        self.ipFile.seek(num)
        numArray = []
        for i in range(num3):
            tmp = bytearray(7)
            self.ipFile.readinto(tmp)
            numArray.append(self.__bytesToNumber(tmp[:4]))
        self.ipFile.seek(num)
        return numArray

    def __readLongX(self, bytesCount):
        rawData = bytearray(self.ipFile.read(bytesCount))
        return self.__bytesToNumber(rawData)

    def __bytesToNumber(self, rawData):
        sum = 0
        for i in rawData[::-1]:
            sum += i
            sum <<= 8

        sum >>= 8
        return sum

    def __searchIP(self, ipArray, start, end):
        index = int((start + end) / 2)
        if index == start:
            return index
        if self.ip < ipArray[index]:
            return self.__searchIP(ipArray, start, index)
        return self.__searchIP(ipArray, index, end)

    def __readString(self, flag):
        if (3,)<sys.version_info:
            if flag == 1 or flag == 2:
                self.ipFile.seek(self.__readLongX(3))
            else:
                self.ipFile.seek(-1, 1)
            rawData = b''
            while True:
                tmp = self.ipFile.read(1)
                if tmp == b'\x00':
                    break
                rawData += tmp
            return str(rawData,'gbk')
        else:
            if flag == 1 or flag == 2:
                self.ipFile.seek(self.__readLongX(3))
            else:
                self.ipFile.seek(-1, 1)
            rawData = b''
            while True:
                tmp = self.ipFile.read(1)
                if tmp == b'\x00':
                    break
                rawData += tmp
            return rawData.decode('gbk')


    def getIPLocation(self, strIP):
        self.ip = self.__ipToLong(strIP)
        ipArray = self.__readIPArray()
        num = int(self.__searchIP(ipArray, 0, len(ipArray) - 1) * 7) + 4
        self.ipFile.seek(num, 1)
        self.ipFile.seek(self.__readLongX(3) + 4, 0)
        location = {}
        flag = self.__readLongX(1)
        if flag == 1:
            self.ipFile.seek(self.__readLongX(3))
            flag = self.__readLongX(1)
        position = self.ipFile.tell()
        location['country'] = self.__readString(flag)
        if flag == 2:
            self.ipFile.seek(position + 3)
        flag = self.__readLongX(1)
        location['area'] = self.__readString(flag)
        self.ipFile.seek(0)
        return location

    def close(self):
        self.ipFile.close()


def findIP(strIP):
    searchCase = IPv4toLocation()
    location = searchCase.getIPLocation(strIP)
    return location


if __name__ == '__main__':
    NUM = 5
    import random, time

    start = time.time()
    for i in range(NUM):
        testCase = IPv4toLocation()
        ipAddress = "%d.%d.%d.%d" % (
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        location = testCase.getIPLocation(ipAddress)
        print(ipAddress, location)
    print("total:{0}, takes:{1}".format(NUM, time.time() - start))
