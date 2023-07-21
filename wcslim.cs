private AmmoDef Example_Ammo => new AmmoDef
{
    AmmoMagazine = "Energy",
BaseDamage = 4261,
    HardPointUsable = true,
    NoGridOrArmorScaling = true, 
    Trajectory = new TrajectoryDef
    {
        MaxLifeTime = 3600,
MaxTrajectory = 7570,
DesiredSpeed = 5740,
    },
    AmmoGraphics = new GraphicDef
    {
	VisualProbability = 1f,
	Lines = new LineDef
	{
	   Tracer = new TracerBaseDef
	   {
	       Enable = true,
	       Length = 10f,
	       Width = 0.1f,
Color = Color(red: 500, green: 200, blue: 50, alpha: 1),
	       Textures = new[] {"ProjectileTrailLine",},
	   },
	},
    },
};


















