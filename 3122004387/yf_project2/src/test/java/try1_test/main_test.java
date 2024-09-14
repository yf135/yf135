package try1_test;

import try1_tool.HammingUtils;
import try1_tool.SimHashUtils;
import try1_tool.TxtIOUtils;
import org.junit.jupiter.api.Test;

public class main_test {

    @Test
    public void origAndAllTest(){
        String[] str = new String[6];
        str[0] = TxtIOUtils.readTxt("D:\\test\\orig.txt");
        str[1] = TxtIOUtils.readTxt("D:\\test\\orig_0.8_add.txt");
        str[2] = TxtIOUtils.readTxt("D:\\test\\orig_0.8_del.txt");
        str[3] = TxtIOUtils.readTxt("D:\\test\\orig_0.8_dis_1.txt");
        str[4] = TxtIOUtils.readTxt("D:\\test\\orig_0.8_dis_10.txt");
        str[5] = TxtIOUtils.readTxt("D:\\test\\orig_0.8_dis_15.txt");
        String ansFileName = "D:\\coding\\yf_project2\\src\\test\\java\\testFile\\ansAll.txt";
        for(int i = 0; i <= 5; i++){
            double ans = HammingUtils.getSimilarity(SimHashUtils.getSimHash(str[0]), SimHashUtils.getSimHash(str[i]));
            TxtIOUtils.writeTxt(ans, ansFileName);
        }
    }


}
