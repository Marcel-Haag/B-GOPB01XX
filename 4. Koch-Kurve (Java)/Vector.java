public class Vector {
    public final double x;
    public final double y;
    public Vector(double x, double y) {
        this.x = x; this.y = y;
    }
    public double length() {
        return Math.sqrt(x*x + y*y);
    }
    public Vector normalized() {
        double len = length();
        return new Vector(x/len, y/len);
    }
    public Vector linearInterpolation(Vector other, double t) {
        return new Vector((1-t)*x + t*other.x, (1-t)*y + t*other.y);
    }
}
