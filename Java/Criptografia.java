import javax.swing.JOptionPane;

public class Criptografia {
    public static void main(String[] args) {
                // Solicita a entrada do usuário
                String entrada = JOptionPane.showInputDialog("Digite a mensagem para criptografar:");
        
                // Converte a string para um vetor de caracteres
                char[] caracteres = entrada.toCharArray();
                
                // Converte os caracteres para inteiros (tabela ASCII) e soma 10 unidades
                int[] valoresAscii = new int[caracteres.length];
                for (int i = 0; i < caracteres.length; i++) {
                    valoresAscii[i] = (int) caracteres[i] + 10;
                }
                
                // Converte os valores ASCII modificados de volta para caracteres
                char[] caracteresCriptografados = new char[valoresAscii.length];
                for (int i = 0; i < valoresAscii.length; i++) {
                    caracteresCriptografados[i] = (char) valoresAscii[i];
                }
                
                // Converte o array de caracteres para uma String final criptografada
                String mensagemCriptografada = new String(caracteresCriptografados);
                
                // Exibe a mensagem criptografada
                JOptionPane.showMessageDialog(null, "Mensagem criptografada: " + mensagemCriptografada);
    }
}v
