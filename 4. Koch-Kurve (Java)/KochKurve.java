/* ... */
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.WindowConstants;
/* ... */
import java.awt.Graphics;
import java.awt.Polygon;

public class KochKurve extends JFrame {
    // Exercise: 1. a)
    public KochKurve(Polygon polygon, int stage) {
        var panel = new JPanel() {
            @Override
            public void paintComponent(Graphics g) {
                if (stage == 0) {
                    g.drawPolygon(polygon);
                } else {
                    int r = 500 / 2;
                    int paddingX = r;
                    int paddingY = 500 / 2;

                    Vector tmpVector = null;

                    for (int i = 0; i < polygon.npoints + 1; i++) {
                        double phi = i * 2 * Math.PI / polygon.npoints;
                        double x = Math.sin(phi) * -r * 0.80;
                        double y = Math.cos(phi) * -r * 0.80;

                        Vector calcVector = new Vector(Math.round(x + paddingX), Math.round(y + paddingY));

                        if (tmpVector != null) {
                            subdivide(g, tmpVector, calcVector, stage);
                        }

                        tmpVector = calcVector;
                    }
                }
            }
        };
        add(panel);
        pack();
        setSize(500, 500);
        setVisible(true);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

    // Exercise: 1. b)
    public static void subdivide(Graphics g, Vector pVector, Vector qVector, int stage) {
        if (stage == 0) {
            Polygon polygon = new Polygon();
            polygon.addPoint((int) Math.round(pVector.x), (int) Math.round(pVector.y));
            polygon.addPoint((int) Math.round(qVector.x), (int) Math.round(qVector.y));
            g.drawPolygon(polygon);
            return;
        }

        Vector R = new Vector(pVector.x * 2 / 3 + qVector.x / 3, pVector.y * 2 / 3 + qVector.y / 3);
        Vector T = new Vector(pVector.x / 3 + qVector.x * 2 / 3, pVector.y / 3 + qVector.y * 2 / 3);
        Vector S = new Vector((int) ((R.x + T.x) / 2 + (R.y - T.y) * Math.sqrt(3) / 2),
                (int) ((R.y + T.y) / 2 + (T.x - R.x) * Math.sqrt(3) / 2));

        --stage;
        subdivide(g, pVector, R, stage);
        subdivide(g, R, S, stage);
        subdivide(g, S, T, stage);
        subdivide(g, T, qVector, stage);
    }

    // Main
    public static void main(String[] args) {
        // Define and initialize [ausgangspolygon]
        Polygon ausgangspolygon = new Polygon();
        ausgangspolygon.addPoint(250, 50);
        ausgangspolygon.addPoint(400, 350);
        ausgangspolygon.addPoint(100, 350);

        // Exercise: 1. c)
        try {
            int inputStage = Integer.parseInt(args[0]);
            switch (inputStage) {
                case 0:
                    // Draw Stage: 0 Koch-Kurve
                    KochKurve k0 = new KochKurve(ausgangspolygon, 0);
                    k0.setTitle("Koch-Kurve");
                    break;
                case 1:
                    // Draw Stage: 1 Koch-Kurve
                    KochKurve k1 = new KochKurve(ausgangspolygon, 1);
                    k1.setTitle("Koch-Kurve: Stufe 1");
                    break;
                case 2:
                    // Draw Stage: 2 Koch-Kurve
                    KochKurve k2 = new KochKurve(ausgangspolygon, 2);
                    k2.setTitle("Koch-Kurve: Stufe 2");
                    break;
                case 3:
                    // Draw Stage: 3 Koch-Kurve
                    KochKurve k3 = new KochKurve(ausgangspolygon, 3);
                    k3.setTitle("Koch-Kurve: Stufe 3");
                    break;
                case 4:
                    // Draw Stage: 4 Koch-Kurve
                    KochKurve k4 = new KochKurve(ausgangspolygon, 4);
                    k4.setTitle("Koch-Kurve: Stufe 4");
                    break;
                case 5:
                    // Draw Stage: 5 Koch-Kurve
                    KochKurve k5 = new KochKurve(ausgangspolygon, 5);
                    k5.setTitle("Koch-Kurve: Stufe 5");
                    break;
                default:
                    System.out.println("Valid case needs to be between 0 and 5.");
                    // Draw Stage: 0 Koch-Kurve for default case
                    KochKurve kDefault = new KochKurve(ausgangspolygon, 0);
                    kDefault.setTitle("Default Koch-Kurve");
                    break;
            }
        } catch(Exception ex) {
            System.out.println("Default Kochkurve for " + ex);
            // Draw Stage: 0 Koch-Kurve for exception case
            KochKurve kExDefault = new KochKurve(ausgangspolygon, 0);
            kExDefault.setTitle("Default exception Koch-Kurve");
        }
    }
}
