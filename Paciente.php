<?php
class Paciente
{
    private $nome;
    private $rg;
    private $cpf;
    private $endereco;
    private $profissao;

    // Getter e Setter para Nome
    public function getNome()
    {
        return $this->nome;
    }
    public function setNome($nome)
    {
        $this->nome = $nome;
    }

    // Getter e Setter para RG
    public function getRg()
    {
        return $this->rg;
    }
    public function setRg($rg)
    {
        $this->rg = $rg;
    }

    // Getter e Setter para CPF
    public function getCpf()
    {
        return $this->cpf;
    }
    public function setCpf($cpf)
    {
        $this->cpf = $cpf;
    }

    // Getter e Setter para Endereço
    public function getEndereco()
    {
        return $this->endereco;
    }
    public function setEndereco($endereco)
    {
        $this->endereco = $endereco;
    }

    // Getter e Setter para Profissão
    public function getProfissao()
    {
        return $this->profissao;
    }
    public function setProfissao($profissao)
    {
        $this->profissao = $profissao;
    }
}
?>
