import Discord from "discord.js";

const client = new Discord.Client();

client.on("ready", () => {
  if (client.user) {
    console.log(`Logged in as ${client.user.tag}!`);
  }
});

client.on("interactionCreate", async (interaction) => {
  if (!interaction.isCommand()) return;
  if (interaction.commandName === "ping") {
    await interaction.reply("Pong!");
  }
});

client.login("ODQ4MTY2ODQ0NzUzNjQxNDcy.YLIq7Q.cw0FJRJ_vKfmhcYhiwY_6dAmeEM");
