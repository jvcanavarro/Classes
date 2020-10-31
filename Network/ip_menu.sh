input="0"
now=$(date +'%d/%m/%Y')


while [ $input != "8" ]
    do
        echo -e "\nOlá, $(whoami).\nHoje é $now."
        echo -e "
                 1- Listar processos
                 2- Listar processos hierarquicamente
                 3- Matar um processo
                 4- Listar configuração de rede
                 5- Testar concetividade com host
                 6- Rastrear pacote em uma rota
                 7- Listar conexões de internet tcp ativas
                 8- Sair\n"

        read input
        case $input in

            1)
                ps ax --forest
                ;;

            2)
                ps ax -H
                ;;

            3)
                echo -n "ID do Processo: "
                read process_id
                echo "Processo $process_id encerrado."
                kill $process_id
                ;;

            4)
                networkctl
                ifconfig -a
                ;;

            5)
                echo -n "Endereço do Host: "
                read address
                ping $address -c 5
                ;;

            6)
                echo -n "Endereço para Traceroute: "
                read address
                traceroute $address
                ;;

            7)
                netstat -tn
                ;;

            8)
                echo "Saindo do Menu."
                ;;

        esac

    done


