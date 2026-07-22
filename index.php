<?php
include_once 'Paciente.php';

$paciente = new Paciente();
$paciente->setNome("Roberto Silva");
$paciente->setRg("45.983.098-6");
$paciente->setCpf("123.456.789-00");
$paciente->setEndereco("Rua Pau Brasil, 123 - São Paulo");
$paciente->setProfissao("Engenheiro de Software");

echo "<strong>Nome:</strong> " . $paciente->getNome() . "<br>";
echo "<strong>RG:</strong> " . $paciente->getRg() . "<br>";
echo "<strong>CPF:</strong> " . $paciente->getCpf() . "<br>";
echo "<strong>Endereço:</strong> " . $paciente->getEndereco() . "<br>";
echo "<strong>Profissão:</strong> " . $paciente->getProfissao() . "<br>";
?>
