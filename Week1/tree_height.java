import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class tree_height {
    class FastScanner {
		StringTokenizer tok = new StringTokenizer("");
		BufferedReader in;

		FastScanner() {
			in = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() throws IOException {
			while (!tok.hasMoreElements())
				tok = new StringTokenizer(in.readLine());
			return tok.nextToken();
		}
		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
	}

	public class TreeHeight {
		int n;
		int parent[];
		
		void read() throws IOException {
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();
			}

		}


		int computeHeight() {
			ArrayList<Integer>[] nodes = new ArrayList[n];

			// Initialize the ArrayLists
			for (int i = 0; i < nodes.length; i++) {
        		nodes[i] = new ArrayList<Integer>();
        	}
			int root = -1;
			for (int i=0; i < n; i++) {
				if (parent[i] == -1) {
					// By the way find and store root
					root = i;
				} else {
					nodes[parent[i]].add(i);
				}
			}
			// Implement BFS queue
			Queue<ArrayList<Integer>> queue = new LinkedList<>();
			//  Store root tree first
			ArrayList<Integer> node = new ArrayList<Integer>();
			node.add(root);
			node.add(1);
			queue.add(node);
			int max_height = 0;

			// While queue is not empty
			while (!queue.isEmpty()) {
				// Remove last queue item
				ArrayList<Integer> current_node = queue.poll();
				int height = current_node.get(1);
				max_height = Math.max(max_height, height);

				// Add other children to the queue
				for (int child: nodes[current_node.get(0)]) {
					ArrayList<Integer> new_node = new ArrayList<Integer>();
					new_node.add(child);
					new_node.add(height+1);
					queue.add(new_node);
				}
			}
			return max_height;
			}

		
	}

	static public void main(String[] args) throws IOException {
            new Thread(null, new Runnable() {
                    public void run() {
                        try {
                            new tree_height().run();
                        } catch (IOException e) {
                        }
                    }
                }, "1", 1 << 26).start();
	}
	public void run() throws IOException {
		TreeHeight tree = new TreeHeight();
		tree.read();
		System.out.println(tree.computeHeight());
	}
}
