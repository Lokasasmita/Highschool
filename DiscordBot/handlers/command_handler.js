const fs = require('fs');

module.exports = (client, Discord) =>{
    const command_Files = fs.readdirSync('./commands/').filter(file => file.endsWith('.js')); 
    //tells the bot which folder to find the commands, and specifically which file type the commands are in
    for(const file of command_Files){
        const command = require(`../commands/${file}`);
        if(command.name){
            client.commands.set(command.name, command);
        }else {
            continue;
        }

    }
}