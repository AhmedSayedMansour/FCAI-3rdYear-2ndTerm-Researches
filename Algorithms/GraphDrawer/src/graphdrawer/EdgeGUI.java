/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graphdrawer;

/**
 *
 * @author ahmed
 */
public class EdgeGUI {

    String src, dest, weight;

    EdgeGUI(String src, String dest, String weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }

    String getSrc() {
        return src;
    }

    String getDest() {
        return dest;
    }

    String getWeight() {
        return weight;
    }
}
