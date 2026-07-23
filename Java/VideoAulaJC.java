import javax.swing.JOptionPane;

public class VideoAulaJC {
    public static void main(String[] args) {
        // INPUTS
        JOptionPane.showMessageDialog(null, "Olá Mundo!", "Programa do Raul", JOptionPane.INFORMATION_MESSAGE);
        int variavelINT = Integer.parseInt(JOptionPane.showInputDialog("Digite um valor inteiro: "));
        double variavelDOUBLE = Double.parseDouble(JOptionPane.showInputDialog("Digite um valor decimal: "));
        String variavelSTRING = JOptionPane.showInputDialog("Digite um valor inteiro: ");

        // EXIBIR OS INPUTS
        JOptionPane.showMessageDialog(null, "O valor inteiro é " + variavelINT, "Programa do Raul", JOptionPane.INFORMATION_MESSAGE);
        JOptionPane.showMessageDialog(null, "O valor decimal é " + variavelDOUBLE, "Programa do Raul", JOptionPane.INFORMATION_MESSAGE);
        JOptionPane.showMessageDialog(null, "O valor em string é " + variavelSTRING, "Programa do Raul", JOptionPane.INFORMATION_MESSAGE);

        char[] caracteres = variavelSTRING.toCharArray(); // Separa cada caractere da mensagem, individualmente
        for (char c: caracteres){
            JOptionPane.showMessageDialog(null, caracteres); // Exibi cada um dos caracteres
        }
    }
}
