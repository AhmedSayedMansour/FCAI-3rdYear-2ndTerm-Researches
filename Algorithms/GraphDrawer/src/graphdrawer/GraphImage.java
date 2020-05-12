/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graphdrawer;
 
import java.awt.Dimension;
import javax.swing.JFrame;
import edu.uci.ics.jung.algorithms.layout.CircleLayout;
import edu.uci.ics.jung.graph.DirectedSparseMultigraph;
import edu.uci.ics.jung.graph.Graph;
import edu.uci.ics.jung.graph.util.EdgeType;
import edu.uci.ics.jung.visualization.VisualizationImageServer;
import edu.uci.ics.jung.visualization.decorators.ToStringLabeller;
import java.util.ArrayList;

public class GraphImage {
    int number ;    //number of vertices
    ArrayList<EdgeGUI> edges;
    
    public GraphImage(int number ,ArrayList<EdgeGUI> edges) {
        this.number = number;
        this.edges = edges;
    }
    
    public VisualizationImageServer getGraphImageServer(){
        Graph<String, String> graph =
        new DirectedSparseMultigraph<String, String>();
        
        for(int i=0 ; i<number ;++i){
            graph.addVertex(Integer.toString(i+1));
        }
        
        char c = 'a';
        for(int i=0 ; i<edges.size() ;++i){
            graph.addEdge("E"+(i+1)+"  "+edges.get(i).getWeight(), edges.get(i).getSrc(), edges.get(i).getDest(), EdgeType.DIRECTED);
        }
        
        VisualizationImageServer vv =
          new VisualizationImageServer(
            new CircleLayout(graph), new Dimension(300, 300));
        
        vv.getRenderContext().setVertexLabelTransformer(new ToStringLabeller());
        vv.getRenderContext().setEdgeLabelTransformer(new ToStringLabeller());
        
        return vv;
    }
}