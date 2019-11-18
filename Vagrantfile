# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

cluster = {
  "config-1" => { :ip => "192.168.16.104", :cpus => 1, :mem => 512, :provision => "config-1/run.sh" },
  "config-2" => { :ip => "192.168.16.105", :cpus => 1, :mem => 512, :provision => "config-2/run.sh" },
  "config-3" => { :ip => "192.168.16.106", :cpus => 1, :mem => 512, :provision => "config-3/run.sh" },
  "query-router" => { :ip => "192.168.16.107", :cpus => 1, :mem => 512, :provision => "query-router/run.sh" },
  "shard-1" => { :ip => "192.168.16.108", :cpus => 1, :mem => 512, :provision => "shard-1/run.sh" },
  "shard-2" => { :ip => "192.168.16.109", :cpus => 1, :mem => 512, :provision => "shard-2/run.sh" }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  cluster.each_with_index do |(hostname, info), index|

    config.vm.define hostname do |node|
      node.vm.hostname = hostname
      node.vm.box = "ubuntu/bionic64"
      node.vm.network :private_network, ip: "#{info[:ip]}"

      node.vm.provider :virtualbox do |vb|
        vb.name = hostname
        vb.gui = false
        vb.memory = info[:mem]
        vb.cpus = info[:cpus]
      end

      node.vm.provision "shell", run: "once", path: info[:provision]
    end

  end

end
