package try1;

import try1_tool.HammingUtils;
import try1_tool.SimHashUtils;
import try1_tool.TxtIOUtils;

public  class main{

        public static void main(String[] args) {

              if (args.length < 3) { System.err.println("��������");
                System.exit(1); }
                // �������������·������ȡ��Ӧ���ļ������ļ�������ת��Ϊ��Ӧ���ַ���
                String str0 =TxtIOUtils.readTxt(args[0]);
                    String str1 = TxtIOUtils.readTxt(args[1]);
                String resultFileName = args[2];
                // ���ַ����ó���Ӧ�� simHashֵ
                String simHash0 = SimHashUtils.getSimHash(str0);
                String simHash1 = SimHashUtils.getSimHash(str1);
                // �� simHashֵ������ƶ�
                double similarity = HammingUtils.getSimilarity(simHash0, simHash1);
                // �����ƶ�д�����Ľ���ļ���
                TxtIOUtils.writeTxt(similarity, resultFileName);
                // �˳�����
                System.exit(0);
         }

}
