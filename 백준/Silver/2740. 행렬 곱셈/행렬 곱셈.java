import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

  static StringBuilder sb = new StringBuilder();
  static int n, m, k;
  static int[][] a, b, answer;

  public static void main(String[] args) throws IOException {
    setUp();

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < k; j++) {
        for (int l = 0; l < m; l++) {
          answer[i][j] += a[i][l] * b[l][j];
        }
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < k; j++) {
        sb.append(answer[i][j]).append(" ");
      }
      sb.append("\n");
    }

    output();
  }

  private static void setUp() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    a = new int[n][m];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        a[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    st = new StringTokenizer(br.readLine());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());
    b = new int[m][k];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < k; j++) {
        b[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    answer = new int[n][k];
  }

  private static void output() throws IOException {
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write(sb.toString());
    bw.flush();
    bw.close();
  }

}