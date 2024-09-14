package try1_tool;

import com.hankcs.hanlp.HanLP;


import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.List;

public class SimHashUtils {

    //传入String，计算出它的hash值，并以字符串形式输出

    public static String getHash(String str){
        try{
            // 这里使用了SHA-256获得hash值
            MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
            return new BigInteger(1, messageDigest.digest(str.getBytes("UTF-8"))).toString(2);
        }catch(Exception e){
            e.printStackTrace();
            return str;
        }
    }


    public static String getSimHash(String str){
        // 文本长度太短时HanLp无法取得关键字

        // 用数组表示特征向量,取128位,从 0 1 2 位开始表示从高位到低位
       // if (str.length() < 200,"text length is too short!");
        int[] v = new int[128];
        // 分词（使用了外部依赖hankcs包提供的接口）
        List<String> keywordList = HanLP.extractKeyword(str, str.length());//取出所有关键词
        // hash
        int size = keywordList.size();
        int i = 0;//以i做外层循环
        for(String keyword : keywordList){
            // 获取hash值
            String keywordHash = getHash(keyword);
            if (keywordHash.length() < 128) {
                // hash值可能少于128位，在低位以0补齐
                int dif = 128 - keywordHash.length();
                for (int j = 0; j < dif; j++) {
                    keywordHash += "0";
                }
            }
            // 加权与合并
            for (int j = 0; j < v.length; j++) {
                // 对keywordHash的每一位与'1'进行比较
                if (keywordHash.charAt(j) == '1') {
                    //权重分10级，由词频从高到低，取权重10~0
                    v[j] += (10 - (i / (size / 10)));
                } else {
                    v[j] -= (10 - (i / (size / 10)));
                }
            }
            i++;
        }
        // 降维
        String simHash = "";// 储存返回的simHash值
        for (int j = 0; j < v.length; j++) {
            // 从高位遍历到低位
            if (v[j] <= 0) {
                simHash += "0";
            } else {
                simHash += "1";
            }
        }
        return simHash;
    }

}