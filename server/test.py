import pytest
import os.path
def test_for_existence():
    assert os.path.exists("packet.bin") == True

def test_for_completeness():
    original = open("../test_client/generate_packet/gprs_packet.bin", "rb")
    downloaded = open("packet.bin", "rb")
    i=0
    while i<89:
        byte_from_org = original.read(1)
        byte_from_dwnl = downloaded.read(1)
        print(byte_from_org, byte_from_dwnl)
        i+=1
        assert byte_from_org == byte_from_dwnl



