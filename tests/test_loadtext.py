"""Test loadtext."""
import pytest
from ezbee.loadtext import loadtext


@pytest.mark.xfail(reason="no file provided, trying to open ’.‘.")
def test1():
    r"""Test default file."""
    text = loadtext()
    # eq_(2283, len(text))
    # eq_(2283, len(text))

    # del text
    if text:
        assert len(text) == 86423


def testgb():
    r"""Test shuangyu_ku\txt-books\19部世界名著中英文对照版TXT."""
    file = r"tests/爱丽丝漫游奇境记.txt"
    text = loadtext(file)
    if text:
        # assert len(text) == 190913
        assert len(text) >= 188760

    text0 = "ALICE'S ADVENTURES IN WONDERLAND\n CHAPTER  01  Down the Rabbit-Hole\n CHAPTER  02  The Pool of Tears\n CHAPTER  03  A Caucus-Race and a Long Tale\n CHAPTER  04  The Rabbit Sends in a Little Bill\n CHAPTER  05  Advice from a Caterpillar\n CHAPTER  06  Pig and Pepper\n CHAPTER  07  A Mad Tea-Party\n CHAPTER  08  The Queen's Croquet-Ground\n CHAPTER  09  The Mock Turtle's Story \n CHAPTER  10  The Lobster Quadrille\n CHAPTER  11  Who Stole the Tarts?\n CHAPTER  12  Alice's Evidence\n\n\n 爱 丽 丝 漫 游 奇 境 记 \n\n 第01章 "  # NOQA

    if text:
        assert text0 == text[:500]


def test_utf_16le():
    r"""Test  'E:\\beta_final_version\\build\\test_files\\files_for_testing_import\\Folding_Beijing_12.txt'."""
    # file = 'E:\\beta_final_version\\build\\test_files\\files_for_testing_import\\Folding_Beijing_12.txt'  # NOQA
    file = r"C:\dl\Dropbox\mat-dir\snippets-mat\pyqt\Sandbox\hp_beta-version_files\test_files\files_for_testing_import\Folding_Beijing_12.txt"  # NOQA
    file = r"C:\dl\Dropbox\mat-dir\pyqt\Sandbox\hp_beta-version_files\test_files\files_for_testing_import\Folding_Beijing_12.txt"
    file = r"tests/Folding_Beijing_12.txt"

    text = loadtext(file)
    if text:
        assert len(text) == 117871

    # text0 = '\ufeffFolding Beijing\t北京折叠\n"by Hao Jingfang, translated by Ken Liu"\t郝景芳\n# 1.\t# 1\n"At ten of five in the m'  # NOQA
    text0 = r'Folding Beijing\t北京折叠\n"by Hao Jingfang, translated by Ken Liu"\t郝景芳\n# 1.\t# 1\n"At ten of five in the mo'  # NOQA
    text2 = 'Folding Beijing\t\xe5\x8c\x97\xe4\xba\xac\xe6\x8a\x98\xe5\x8f\xa0\r\n"by Hao Jingfang, translated by Ken Liu"\t\xe9\x83\x9d\xe6\x99\xaf\xe8\x8a\xb3\r\n# 1.\t# 1\r\n"At ten of five in the mo'

    del text2

    # if text: assert text0 == text[:100]
