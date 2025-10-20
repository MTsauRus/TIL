package backend.JAVA.intermediate;

public class ThreadYield {
    public static class WorkThread extends Thread { // static을 붙여야 main에서 바로 사용 가능, main이 static이기 때문
        public boolean work = true;
        public WorkThread(String name) {
            setName(name);
        }

        @Override
        public void run() {
            while (true) {
                if (work) {
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                    System.out.println(getName() + " 작업 중...");
                } else {
                    Thread.yield();
                }
            }
        }
    }
    public static void main(String[] args) {
        WorkThread wt1 = new WorkThread("thread1");
        WorkThread wt2 = new WorkThread("thread2");
        wt1.start();
        wt2.start();

        try { Thread.sleep(2000); } catch (InterruptedException e) { }
        wt1.work = false;
        System.out.println("thread1 작업 중지");
        try { Thread.sleep(2000); } catch (InterruptedException e) { }
        wt1.work = true;
        System.out.println("thread1 작업 재개");
    }
}
