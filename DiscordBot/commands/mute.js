const ms = require('ms');

module.exports = {
    name: 'mute',
    category: "Moderation",
    description: "This command mutes a member for a certain period of time",
    execute(client, message, args, Discord) {
        const target = message.mentions.users.first();

        if(!target){
            return message.reply("Please mention a valid member of the server");
        }

        let muteRole = message.guild.roles.cache.find(role => role.name === 'Muted')
        if (!muteRole){
            return message.reply("There is no Muted role on this server");
        }

        if (!args[1]) {
            let memberTarget = message.guild.members.cache.get(target.id);
            memberTarget.roles.add(muteRole.id);
            message.channel.send(`<@${memberTarget.user.id}> has been muted`);
            return
        }

        let memberTarget = message.guild.members.cache.get(target.id);
        memberTarget.roles.add(muteRole.id);
        message.channel.send(`<@${memberTarget.user.id}> has been muted for ${ms(ms(args[1]))}`);

        setTimeout(function () {
            memberTarget.roles.remove(muteRole.id);
            message.channel.send(`<@${memberTarget.user.id}> has been unmuted`)
        }, ms(args[1]));


    }
}