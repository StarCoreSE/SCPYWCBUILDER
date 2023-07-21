private AmmoDef Example_Ammo => new AmmoDef
{
    AmmoMagazine = "Energy",
    BaseDamage = 100,
    HardPointUsable = true,
    NoGridOrArmorScaling = true, 
    Trajectory = new TrajectoryDef
    {
        MaxLifeTime = 3600,
	MaxTrajectory = 300,
	DesiredSpeed = 300,
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
	       Color = Color(red: 5, green: 2, blue: 1f, alpha: 1),
	       Textures = new[] {"ProjectileTrailLine",},
	   },
	},
    },
};